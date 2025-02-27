from collections import defaultdict

def palindrome_of_length_at_least_n(s: str) -> set[str]:
    answer = set()
    char_counts = defaultdict(int)
    for char in s:
        char_counts[char] += 1
    for char, count in char_counts.items():
        if char.isalpha():
            for i in range(26):
                if char + i in char_counts:
                    answer.add(char * count + (char + i) * i)
    return answer
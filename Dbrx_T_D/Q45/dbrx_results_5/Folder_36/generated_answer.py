from collections import defaultdict

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substring = s[5:9].lower()
    char_count = defaultdict(int)
    for char in substring:
        if char.isalpha():
            char_count[char] += 1
    palindromes = set()
    for first, first_count in char_count.items():
        for second, second_count in char_count.items():
            if first == second and first_count < 2:
                continue
            count = min(first_count, second_count)
            for _ in range(count):
                for leave_one_out in range(first_count):
                    palindrome = first * (first_count - leave_one_out - 1) + second * (second_count - count) + first * leave_one_out
                    palindromes.add(palindrome)
    palindromes = {palindrome for palindrome in palindromes if len(palindrome) >= 3}
    return palindromes
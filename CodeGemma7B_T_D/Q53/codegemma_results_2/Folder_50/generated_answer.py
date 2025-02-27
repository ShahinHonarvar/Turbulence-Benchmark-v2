from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    char_frequencies = defaultdict(int)
    for char in text:
        char_frequencies[char] += 1
    palindrome_sets = defaultdict(set)
    for char, frequency in char_frequencies.items():
        half_palindrome = char * (frequency // 2)
        palindrome_sets[frequency].add(half_palindrome)
    result = set()
    for frequency in range(91, 0, -1):
        if frequency in palindrome_sets:
            for half_palindrome in palindrome_sets[frequency]:
                if frequency % 2 == 0 and half_palindrome * 2 in text or (frequency % 2 == 1 and half_palindrome * 2 + char in text):
                    palindrome = half_palindrome * 2 + half_palindrome[::-1]
                    result.add(palindrome)
    return sorted(result)
from collections import Counter
    import math

def palindromes_between_indices(s):
    frequent_chars = Counter(s)
    chars = s[1:9]
    char_counter = Counter(chars)
    even_chars = [k for k, v in char_counter.items() if v % 2 == 0]
    frequent_even_chars = [k for k, v in frequent_chars.items() if v > len(s) / 2 and k in even_chars]
    if not frequent_even_chars:
        return set()
    palindrome_set = set()
    for p in range(len(even_chars)):
        for q in range(p + 1, len(even_chars)):
            n = char_counter[even_chars[p]] + char_counter[even_chars[q]]
            palindrome = even_chars[p] * (n // 2) + even_chars[q] * (n // 2)
            if len(palindrome) >= 4:
                palindrome_set.add(palindrome)
    return palindrome_set
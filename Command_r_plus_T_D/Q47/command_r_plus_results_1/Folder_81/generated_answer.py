def palindromes_of_specific_lengths(s: str) -> set:

    def is_palindrome(sub_s: str) -> bool:
        return sub_s.lower() == sub_s.lower()[::-1]
    result = set()
    for length in range(12, 221):
        for start in range(12, 123 - length):
            sub_s = s[start:start + length]
            if sub_s.isalpha() and is_palindrome(sub_s):
                result.add(sub_s)
    return result
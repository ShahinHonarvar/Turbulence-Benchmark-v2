def palindromes_of_specific_lengths(s: str) -> set:

    def is_palindrome(sub_s: str) -> bool:
        return sub_s.lower() == sub_s.lower()[::-1]
    palindromes = set()
    substring = s[15:61]
    for length in range(16, 40):
        for i in range(len(substring) - length + 1):
            sub_s = substring[i:i + length]
            if sub_s.isalpha() and is_palindrome(sub_s):
                palindromes.add(sub_s)
    return palindromes
def palindrome_of_length_at_least_n(s: str) -> set:

    def is_palindrome(sub_s: str) -> bool:
        return sub_s.lower() == sub_s.lower()[::-1]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 144, len(s) + 1):
            sub_s = s[i:j]
            if sub_s.isalpha() and is_palindrome(sub_s):
                palindromes.add(sub_s)
    return palindromes
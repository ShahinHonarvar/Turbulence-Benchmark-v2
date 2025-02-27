def palindromes_between_indices(s: str) -> set:

    def is_palindrome(s):
        return s == s[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    sub_str = ''.join(filter(english_letters.__contains__, s[3:9]))
    return set((sub_str[i:j] for i in range(len(sub_str)) for j in range(i + 5, len(sub_str) + 1) if is_palindrome(sub_str[i:j])))
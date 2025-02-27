def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = s[18:66]
    result = set()
    clean_str = ''.join((ch for ch in s if ch.isalpha())).lower()
    for length in range(23, 37):
        for i in range(len(clean_str) - length + 1):
            substring = clean_str[i:i + length]
            if is_palindrome(substring):
                result.add(substring)
    return result
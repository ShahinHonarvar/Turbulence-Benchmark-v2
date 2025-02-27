def palindrome_of_length_at_least_n(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    palindromes = set()
    clean_s = ''.join(filter(str.isalpha, s)).lower()
    length = len(clean_s)
    for start in range(length):
        for end in range(start + 98, length + 1):
            substring = clean_s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes
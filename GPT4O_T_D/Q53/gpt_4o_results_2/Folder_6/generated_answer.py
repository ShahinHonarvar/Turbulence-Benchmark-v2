def is_palindrome(s):
    return s == s[::-1]

def find_all_palindromes(s, min_length):
    palindromes = set()
    length = len(s)
    for start in range(length):
        for end in range(start + min_length, length + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes

def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    return find_all_palindromes(s, 22)
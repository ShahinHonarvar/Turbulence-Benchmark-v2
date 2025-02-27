def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        sub = sub.lower()
        return sub == sub[::-1]

    def is_valid_char(c):
        return 'a' <= c <= 'z' or 'A' <= c <= 'Z'
    s = ''.join(filter(is_valid_char, s))
    substr = s[:21]
    palindromes = set()
    for start in range(len(substr)):
        for end in range(start + 5, min(len(substr), start + 81)):
            potential_palindrome = substr[start:end + 1]
            if is_palindrome(potential_palindrome):
                palindromes.add(potential_palindrome)
    return palindromes
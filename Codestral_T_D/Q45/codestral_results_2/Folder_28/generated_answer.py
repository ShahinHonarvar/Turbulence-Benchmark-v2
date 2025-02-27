def palindromes_between_indices(s):
    s = s[1:6].lower()
    result = set()

    def is_palindrome(string):
        return string == string[::-1]

    def generate_palindromes(string, curr='', start=0):
        if len(curr) >= 4 and is_palindrome(curr):
            result.add(curr)
        for i in range(start, len(string)):
            generate_palindromes(string, curr + string[i], i + 1)
    generate_palindromes(s)
    return result
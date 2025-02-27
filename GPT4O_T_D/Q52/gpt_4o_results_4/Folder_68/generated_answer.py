def palindrome_of_length_n(s):
    result = set()
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    for i in range(n - 75):
        potential_palindrome = s[i:i + 76]
        if potential_palindrome == potential_palindrome[::-1]:
            result.add(potential_palindrome)
    return result
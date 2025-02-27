def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 92, len(s) + 1):
            potential_palindrome = s[i:j]
            if potential_palindrome == potential_palindrome[::-1]:
                result.add(potential_palindrome)
    return result
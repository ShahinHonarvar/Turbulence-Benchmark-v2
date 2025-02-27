def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 23, len(s) + 1):
            possible_palindrome = s[i:j].lower()
            if possible_palindrome == possible_palindrome[::-1] and possible_palindrome.isalpha():
                result.add(possible_palindrome)
    return result
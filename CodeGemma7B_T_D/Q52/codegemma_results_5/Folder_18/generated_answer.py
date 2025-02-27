def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 391):
        for j in range(i + 1, min(i + 392 + 1, len(s))):
            if is_palindrome(s[i:j]):
                result.add(s[i:j].lower())
    return result

def is_palindrome(s):
    return s == s[::-1]
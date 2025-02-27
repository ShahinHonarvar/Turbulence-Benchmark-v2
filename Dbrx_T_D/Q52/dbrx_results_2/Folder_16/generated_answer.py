def palindrome_of_length_n(string):
    valid_palindromes = set()
    string = string.lower()
    n = len(string)
    for i in range(n - 255 + 1):
        palindrome = string[i:i + 255]
        is_palindrome = True
        for j in range(127):
            if palindrome[j] != palindrome[255 - j - 1]:
                is_palindrome = False
                break
        if is_palindrome:
            valid_palindromes.add(palindrome)
    return valid_palindromes
def palindrome_of_length_n(string):
    string_lower = string.lower()
    set_palindrome = set()
    length_substring = 279
    for i in range(len(string)):
        for j in range(i + length_substring, len(string) + 1):
            substring = string_lower[i:j]
            if substring == substring[::-1] and substring.isalpha():
                set_palindrome.add(substring)
    return set_palindrome
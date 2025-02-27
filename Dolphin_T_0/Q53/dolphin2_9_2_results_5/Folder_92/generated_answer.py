def palindrome_of_length_at_least_n(string):
    string = string.lower()
    set_palindromes = set()
    length_string = len(string)
    for i in range(length_string):
        for j in range(i + 10, length_string + 1):
            subsring = string[i:j]
            if subsring == subsring[::-1] and subsring.isalpha():
                set_palindromes.add(subsring)
    return set_palindromes
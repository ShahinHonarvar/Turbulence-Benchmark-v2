def palindrome_of_length_at_least_n(string):
    string = string.lower()
    all_palindromes = set()
    for char_index in range(len(string)):
        for length in range(95, len(string) - char_index + 1):
            substring = string[char_index:char_index + length]
            if substring == substring[::-1]:
                all_palindromes.add(substring)
    return all_palindromes
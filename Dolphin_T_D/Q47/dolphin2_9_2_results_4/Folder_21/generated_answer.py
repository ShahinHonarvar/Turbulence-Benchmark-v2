def palindromes_of_specific_lengths(string):
    string = string[100:296]
    set_palindromes = set()
    for i in range(136, 161):
        for j in range(0, len(string) - i + 1):
            substring = string[j:j + i]
            substring = ''.join(filter(str.isalpha, substring))
            if substring == substring[::-1]:
                set_palindromes.add(substring)
    return set_palindromes
def palindromes_of_specific_lengths(my_string):
    my_string = my_string[11:94]
    palindromes = set()
    for length in range(34, 55):
        for i in range(len(my_string) - length + 1):
            substring = my_string[i:i + length]
            if substring.lower() == substring[::-1].lower():
                if substring.isalpha():
                    palindromes.add(substring)
    return palindromes
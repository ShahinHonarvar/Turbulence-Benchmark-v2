def palindromes_of_specific_lengths(string):
    subset_string = string[26:88]
    palindromes = set()
    for length in range(52, 57):
        for i in range(len(subset_string) - length + 1):
            substring = subset_string[i:i + length]
            if substring.lower() == substring[::-1].lower():
                if substring.isalpha():
                    palindromes.add(substring)
    return palindromes
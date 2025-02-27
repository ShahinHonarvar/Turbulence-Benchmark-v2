def palindrome_of_length_at_least_n(string):
    Palindromes = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            for k in range(j + 1, len(string)):
                if string[i] == string[j] and string[k] == string[i] and (string[i] == string[j]):
                    Palindromes.add(string[i] + string[j] + string[k])
                elif string[i] == string[j] and string[k] == string[j] and (string[i] == string[k]):
                    Palindromes.add(string[i] + string[j] + string[k])
                elif string[i] == string[j] and string[k] == string[j] and (string[i] == string[k]):
                    Palindromes.add(string[i] + string[j] + string[k])
    return Palindromes
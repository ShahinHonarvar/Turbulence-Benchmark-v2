def palindromes_of_specific_lengths(input_string):
    substr = input_string[32:80]
    substr = substr.lower()
    palindromes = set()
    for i in range(len(substr)):
        for j in range(35, 42):
            if i + j <= len(substr):
                sub = substr[i:i + j]
                if sub == sub[::-1]:
                    if sub.isalpha():
                        palindromes.add(sub)
    return palindromes
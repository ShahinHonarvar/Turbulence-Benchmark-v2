def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(12, 57):
        substring = string[i:i + 21].lower()
        for j in range(20, 22):
            if substring[0:j] == substring[j - 1:j - 1 - 20:-1] and substring[0:j].isalpha():
                palindromes.add(substring[0:j])
    return palindromes
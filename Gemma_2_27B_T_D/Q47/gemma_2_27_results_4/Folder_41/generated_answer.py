def palindromes_of_specific_lengths(text):
    sub_string = text[1:8]
    palindromes = set()
    for i in range(len(sub_string) - 2):
        for j in range(i + 3, len(sub_string) + 1):
            substring = sub_string[i:j].lower()
            if substring == substring[::-1] and 3 <= len(substring) <= 4 and substring.isalpha():
                palindromes.add(substring)
    return palindromes
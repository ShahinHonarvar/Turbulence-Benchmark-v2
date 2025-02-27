def palindromes_of_specific_lengths(text):
    letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    text_of_interest = text[26:78]
    palindromes = set()
    for i in range(len(text_of_interest) - 17):
        for j in range(i + 18, len(text_of_interest) + 1):
            substring = text_of_interest[i:j]
            if substring == substring[::-1] and all((char in letters for char in substring)):
                palindromes.add(substring)
    return palindromes
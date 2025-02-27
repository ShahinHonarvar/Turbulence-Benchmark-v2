def palindromes_between_indices(text):
    text = text.lower()
    text = text[3:6]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            for k in range(j + 1, len(text)):
                for l in range(k + 1, len(text)):
                    palindrome = text[i] + text[j] + text[k] + text[l]
                    palindromes.add(palindrome)
    return palindromes
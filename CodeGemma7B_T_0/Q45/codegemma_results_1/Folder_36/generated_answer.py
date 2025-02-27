def palindromes_between_indices(text):
    text = text.lower()
    text = text[5:9]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 1, len(text)):
            for k in range(j + 1, len(text)):
                palindrome = text[i] + text[j] + text[k]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    if not palindromes:
        return set()
    return palindromes
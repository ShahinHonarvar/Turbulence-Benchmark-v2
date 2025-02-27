def palindromes_between_indices(text):
    text = text.lower()
    palindromes = set()
    for i in range(2, 5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                if text[i] in 'abcdefghijklmnopqrstuvwxyz' and text[j] in 'abcdefghijklmnopqrstuvwxyz' and (text[k] in 'abcdefghijklmnopqrstuvwxyz'):
                    palindrome = text[i] + text[j] + text[k]
                    palindromes.add(palindrome)
    return palindromes
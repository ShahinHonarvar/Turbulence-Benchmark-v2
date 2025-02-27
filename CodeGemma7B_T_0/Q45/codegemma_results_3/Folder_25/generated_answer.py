def palindromes_between_indices(text):
    text = text.lower()
    palindromes = set()
    for i in range(1, 5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                for l in range(k + 1, 5):
                    if text[i] in 'abcdefghijklmnopqrstuvwxyz' and text[j] in 'abcdefghijklmnopqrstuvwxyz' and (text[k] in 'abcdefghijklmnopqrstuvwxyz') and (text[l] in 'abcdefghijklmnopqrstuvwxyz'):
                        palindromes.add(text[i:l + 1])
    return palindromes
def palindromes_of_specific_lengths(str1):
    str2 = str1[15:95]
    filtered_palindromes = []
    for word in str2.lower().split():
        word = word.lower()
        if len(word) >= 39 and len(word) <= 52 and (word == word[::-1]):
            filtered_palindromes.append(word)
    return set(filtered_palindromes)
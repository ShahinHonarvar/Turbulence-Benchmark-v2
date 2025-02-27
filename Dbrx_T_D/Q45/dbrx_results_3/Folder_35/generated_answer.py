def palindromes_between_indices(english_text):
    english_text = english_text[2:5].lower()
    palindromes = set()
    for i in range(len(english_text) - 1):
        for j in range(i, len(english_text)):
            if english_text[i:j + 1] == english_text[i:j + 1][::-1]:
                palindromes.add(english_text[i:j + 1])
    return {palindrome for palindrome in palindromes if len(palindrome) >= 4}
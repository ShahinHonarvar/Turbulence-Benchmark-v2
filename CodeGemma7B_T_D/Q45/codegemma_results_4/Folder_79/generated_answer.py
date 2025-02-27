def palindromes_between_indices(text):
    palindrome_list = []
    for i in range(len(text) - 3):
        for j in range(i + 1, len(text) - 2):
            for k in range(j + 1, len(text) - 1):
                word = text[i:k + 1]
                word = word.lower()
                if word == word[::-1]:
                    palindrome_list.append(word.capitalize())
    if not palindrome_list:
        return set()
    return set(palindrome_list)
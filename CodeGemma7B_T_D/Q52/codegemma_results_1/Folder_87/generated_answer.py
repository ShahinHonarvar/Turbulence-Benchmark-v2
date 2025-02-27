def palindrome_of_length_n(input):
    palindromes = set()
    word = input.lower()
    for i in range(len(word)):
        for j in range(i + 57, len(word)):
            if word[i:j] == word[j - 57:j][::-1]:
                palindromes.add(word[i:j])
    if not palindromes:
        return set()
    return palindromes
def palindromes_between_indices(string):
    letters = [char for char in string[7:10].lower() if char.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 2, len(letters) + 1):
            sub_word = letters[i:j]
            if len(sub_word) >= 3 and sub_word == sub_word[::-1]:
                palindromes.add(''.join(sub_word))
    return palindromes
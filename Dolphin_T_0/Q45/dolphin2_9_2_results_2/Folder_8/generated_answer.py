def palindromes_between_indices(str_input):
    eng_letters = 'abcdefghijklmnopqrstuvwxyz'
    sub_str = str_input[1:6].lower()
    palindromes = set()
    for word in sub_str:
        if len(word) < 5:
            continue
        if all((elem in eng_letters for elem in word)):
            rev_str = word[::-1]
            if word == rev_str:
                palindromes.add(word)
    return palindromes
def palindromes_between_indices(my_str):
    my_str = my_str.lower()
    s = set()
    for i in range(2, 9):
        for j in range(i + 1, 10):
            word = my_str[i - 1:j + 1]
            if word == word[::-1]:
                s.add(word)
    return s
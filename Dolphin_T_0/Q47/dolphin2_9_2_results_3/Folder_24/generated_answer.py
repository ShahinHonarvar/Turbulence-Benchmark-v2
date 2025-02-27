def palindromes_of_specific_lengths(my_string):
    my_string = my_string[11:92]
    result = set()
    for i in range(41, 77):
        for j in range(0, len(my_string) - i + 1):
            sub = my_string[j:j + i]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub.lower())
    return result
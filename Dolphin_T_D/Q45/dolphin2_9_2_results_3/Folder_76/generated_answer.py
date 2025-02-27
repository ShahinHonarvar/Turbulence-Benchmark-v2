def palindromes_between_indices(string):
    string = string[1:5]
    palin_set = set()
    for i in range(len(string)):
        for j in range(i + 3, len(string) + 1):
            sub_string = string[i:j]
            sub_string_set = set(sub_string.lower())
            if sub_string == sub_string[::-1] and sub_string_set.issubset({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}):
                palin_set.add(sub_string)
    return palin_set
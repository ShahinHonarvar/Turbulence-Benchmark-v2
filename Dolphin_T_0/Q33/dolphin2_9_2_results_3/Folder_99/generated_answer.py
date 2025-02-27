def return_vowels(string):
    vowels = 'aeiouAEIOU'
    index_start = 323
    index_end = 526
    result = []
    for index in range(index_start, index_end):
        if '+' < string[index] <= ':' and string[index] in vowels:
            result.append(string[index])
    return result
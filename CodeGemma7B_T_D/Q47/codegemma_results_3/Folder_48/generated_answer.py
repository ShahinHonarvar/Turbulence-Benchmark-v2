from string import ascii_lowercase

def palindromes_of_specific_lengths(str):
    index_range = range(155, 284)
    length_range = range(104, 121)
    result = set()
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if i in index_range and j in index_range and (j - i in length_range):
                word = str[i:j + 1]
                if word == word[::-1].lower():
                    result.add(word)
    return result
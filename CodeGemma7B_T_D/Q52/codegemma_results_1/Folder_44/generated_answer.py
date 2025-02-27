import itertools

def palindrome_of_length_n(text):
    result = set()
    for i, j in itertools.combinations_with_replacement(range(len(text)), 2):
        if i <= j and text[i].lower() == text[j].lower():
            substring = text[i:j + 1]
            if len(substring) == 445:
                result.add(substring)
    return result
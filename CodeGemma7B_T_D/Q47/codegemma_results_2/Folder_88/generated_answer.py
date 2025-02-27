from string import ascii_lowercase as alphabet

def palindromes_of_specific_lengths(text):
    output = set()
    start = 11
    end = 87
    for i in range(start, end + 1):
        for length in range(4, 6):
            for j in range(length):
                phrase = text[i:i + j + 1]
                if phrase == phrase.lower() and phrase.isalpha() and (len(phrase) == length):
                    output.add(phrase.lower())
    return output
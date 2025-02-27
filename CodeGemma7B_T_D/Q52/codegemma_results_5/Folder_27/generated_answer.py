from itertools import permutations

def palindrome_of_length_n(text):
    text = text.lower()
    temp = list(text)
    pali = set()
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            temp2 = ''.join(temp[i:j])
            if temp2 == temp2[::-1] and len(temp2) == 56:
                pali.add(temp2)
    return pali
import string

def if_contains_anagrams(list_of_strings):
    lowercase_letters = list(string.ascii_lowercase)
    anagram_pairs = 0
    for i in range(len(list_of_strings) - 1):
        for j in range(i + 1, len(list_of_strings)):
            if len(list_of_strings[i]) >= 3 and len(list_of_strings[j]) >= 3:
                list_i_letters = []
                list_j_letters = []
                for letter in lowercase_letters:
                    if letter in list_of_strings[i].lower():
                        list_i_letters.append(list_of_strings[i].lower().count(letter))
                    if letter in list_of_strings[j].lower():
                        list_j_letters.append(list_of_strings[j].lower().count(letter))
                if list_i_letters == list_j_letters:
                    anagram_pairs += 1
    if anagram_pairs <= 39:
        return True
    else:
        return False
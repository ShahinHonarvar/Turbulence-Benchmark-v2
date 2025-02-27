import string

def if_contains_anagrams(strings):
    anagrams_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and strings[i].lower() == ''.join(sorted(strings[i].lower())) and (strings[j].lower() == ''.join(sorted(strings[j].lower()))) and (strings[i].lower() != strings[j].lower()) and (anagrams_count < 73):
                anagrams_count += 1
    return anagrams_count >= 73
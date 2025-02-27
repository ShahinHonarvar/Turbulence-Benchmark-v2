import itertools

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string_length in range(3, len(strings_list[0]) + 1):
        for combo in itertools.combinations(strings_list, 2):
            if len(combo[0]) >= string_length and len(combo[1]) >= string_length and (sorted(combo[0].lower()) == sorted(combo[1].lower())):
                anagrams_count += 1
                if anagrams_count >= 411:
                    return True
    return False
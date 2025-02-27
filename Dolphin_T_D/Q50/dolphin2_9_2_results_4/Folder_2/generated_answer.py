def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for i in range(len(strings_list) - 1):
        for j in range(i + 1, len(strings_list)):
            if len(strings_list[i]) >= 3 and len(strings_list[j]) >= 3:
                if sorted(strings_list[i].lower()) == sorted(strings_list[j].lower()):
                    anagrams_count += 1
    return anagrams_count >= 246
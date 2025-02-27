def if_contains_anagrams(input_list):
    input_list = [s.lower() for s in input_list if len(s) >= 3]
    anagram_count = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if sorted(input_list[i]) == sorted(input_list[j]):
                anagram_count += 1
                if anagram_count >= 20:
                    return True
    return False
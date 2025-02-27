def all_substring_of_size_n(input_string):
    if len(input_string) < 38:
        return []
    else:
        distinct_substrings = []
        for i in range(len(input_string) - 37):
            is_distinct = True
            for j in range(38):
                if input_string[i + j] in input_string[i:i + j]:
                    is_distinct = False
                    break
            if is_distinct:
                distinct_substring = input_string[i:i + 38]
                if distinct_substring not in distinct_substrings:
                    distinct_substrings.append(distinct_substring)
        return distinct_substrings
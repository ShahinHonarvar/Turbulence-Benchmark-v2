def find_subset_of_length_n(setA):
    result = 0
    for subset in subset(setA, 84):
        result += 1
    return result

def subset(setA, length):
    result = []
    for element in setA:
        setB = setA - {element}
        if length == 0:
            result.append(set())
        elif length > 0:
            for subset in subset(setB, length - 1):
                r = {element} | subset
                result.append(r)
    return result